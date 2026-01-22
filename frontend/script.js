function analyze() {
    const log = document.getElementById("logInput").value;

    fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({log: log})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText = data.root_cause;
    });
}
