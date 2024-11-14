let RunSentimentAnalysis = () => {
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                // Success: Display the emotion analysis result
                document.getElementById("system_response").innerHTML = JSON.stringify(JSON.parse(xhttp.responseText), null, 2);
            } else if (this.status == 400) {
                // Error: Display the error message
                const errorResponse = JSON.parse(xhttp.responseText);
                document.getElementById("system_response").innerHTML = errorResponse.error;
            }
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}
