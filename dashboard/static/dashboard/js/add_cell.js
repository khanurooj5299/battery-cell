//adding submit event listerner for form
document.getElementById("cellCreationForm").addEventListener("submit", (formEvent) => {
  formEvent.preventDefault();
  //attach image_data_url on submit
  const imageInput = document.getElementById("cellImage");
  if (imageInput.files && imageInput.files[0]) {
    const fileReader = new FileReader();
    // Read the selected file as data URL
    fileReader.readAsDataURL(imageInput.files[0]);
    fileReader.onload = (event)=>{
      const image_data_url = event.target.result;
      document.getElementById('image_data_url').value = image_data_url;
      //submit the form once the dataURL is available
      formEvent.target.submit();
    };
  }
});
