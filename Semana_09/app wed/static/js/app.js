"use strict";

const startButton = document.getElementById("start-camera");
const captureButton = document.getElementById("capture-photo");
const stopButton = document.getElementById("stop-camera");
const video = document.getElementById("camera");
const canvas = document.getElementById("canvas");
const feedback = document.getElementById("feedback");
const uploadForm = document.getElementById("upload-form");
const photoInput = document.getElementById("photos");
const clearForm = document.getElementById("clear-form");

let cameraStream = null;
let uploading = false;

function showMessage(message, type = "info") {
    feedback.replaceChildren();

    const alert = document.createElement("div");
    alert.className = `alert alert-${type}`;
    alert.setAttribute("role", "status");
    alert.textContent = message;

    feedback.appendChild(alert);
}

async function startCamera() {
    if (!navigator.mediaDevices?.getUserMedia) {
        showMessage(
            "La cámara requiere localhost o una conexión HTTPS.",
            "warning"
        );
        return;
    }

    try {
        cameraStream = await navigator.mediaDevices.getUserMedia({
            video: { facingMode: { ideal: "environment" } },
            audio: false
        });

        video.srcObject = cameraStream;
        video.hidden = false;

        await video.play();

        startButton.disabled = true;
        captureButton.disabled = false;
        stopButton.disabled = false;

        showMessage("Cámara lista.", "success");
    } catch {
        showMessage(
            "No se pudo abrir la cámara. Revisa los permisos del navegador.",
            "warning"
        );
    }
}

function stopCamera() {
    if (cameraStream) {
        cameraStream.getTracks().forEach(track => track.stop());
        cameraStream = null;
    }

    video.srcObject = null;
    video.hidden = true;
    startButton.disabled = false;
    captureButton.disabled = true;
    stopButton.disabled = true;
}

async function capturePhoto() {
    if (!cameraStream || !video.videoWidth || uploading) {
        showMessage("Abre la cámara antes de capturar.", "warning");
        return;
    }

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    canvas.getContext("2d").drawImage(
        video, 0, 0, canvas.width, canvas.height
    );

    const blob = await new Promise(resolve =>
        canvas.toBlob(resolve, "image/jpeg", 0.9)
    );

    if (!blob) {
        showMessage("No se pudo capturar la fotografía.", "danger");
        return;
    }

    uploading = true;
    captureButton.disabled = true;

    try {
        const formData = new FormData();
        formData.append("photo", blob, "captura.jpg");

        const response = await fetch("/upload", {
            method: "POST",
            body: formData,
            headers: { "X-Requested-With": "fetch" }
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || "No se pudo guardar la foto.");
        }

        window.location.reload();
    } catch (error) {
        showMessage(error.message, "warning");
    } finally {
        uploading = false;
        captureButton.disabled = !cameraStream;
    }
}

startButton.addEventListener("click", startCamera);
captureButton.addEventListener("click", capturePhoto);
stopButton.addEventListener("click", stopCamera);

uploadForm.addEventListener("submit", event => {
    const files = Array.from(photoInput.files);

    if (files.length === 0) {
        event.preventDefault();
        showMessage("Selecciona al menos una fotografía.", "warning");
        return;
    }

    const totalSize = files.reduce((sum, file) => sum + file.size, 0);

    if (totalSize > 5 * 1024 * 1024) {
        event.preventDefault();
        showMessage(
            "El tamaño total de las fotos no puede superar 5 MB.",
            "warning"
        );
    }
});

clearForm.addEventListener("submit", event => {
    if (!window.confirm("¿Vaciar la estructura seleccionada?")) {
        event.preventDefault();
    }
});

window.addEventListener("pagehide", stopCamera);
