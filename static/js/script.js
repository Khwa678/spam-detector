function checkSpam() {
    const msg = document.getElementById("message").value;
    const resultDiv = document.getElementById("result");

    if (!msg.trim()) {
        resultDiv.innerText = "⚠ Please enter a message";
        return;
    }

    fetch('/api/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        resultDiv.innerText = data.result;
    });
}

function fill(el) {
    document.getElementById("message").value = el.innerText;
}
