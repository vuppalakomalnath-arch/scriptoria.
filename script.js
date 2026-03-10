async function generateScript(){

    let idea = document.getElementById("idea").value;

    const response = await fetch("/generate_script", {
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({prompt:idea})
    });

    const data = await response.json();

    document.getElementById("output").innerText = data.script;
}