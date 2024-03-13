//adding event listener to submit action to get the visualization template from backend and put it in the placed hook in cell-detail template
document
  .getElementById("datasetForm")
  .addEventListener("submit", async (event) => {
    event.preventDefault();
    //request body will contain file as formData
    const formData = new FormData();
    const dataset = document.getElementById("datasetInput").files[0];
    formData.append("dataset", dataset);
    // for django csrf protection
    formData.append(
      "csrfmiddlewaretoken",
      event.target.firstElementChild.value
    );
    //sending the request
    const response = await fetch("/dashboard/cell-visualization", {
      method: "POST",
      body: formData,
    });
    const template = await response.text();
    //getting the hook and attaching the recieved template
    const hook = document.querySelector(".visualization");
    hook.innerHTML = template;
    hook.scrollIntoView();
  });
