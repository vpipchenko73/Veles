
// Read book
    function readDogModalForm() {
      document.addEventListener('DOMContentLoaded', (e) => {
        var readDog = document.getElementsByClassName("read-dog");
        for (var index=0; index < readDog.length; index++) {
          modalForm(readDog[index], {formURL: readDog[index]["dataset"]["formUrl"]});
        }
      });
    };
   readDogModalForm();

// Create-message
    function messageCreateModalForm() {
     document.addEventListener('DOMContentLoaded', (e) => {
     data=document.getElementById('message-create')
     modalForm( data, {formURL: data["dataset"]["formUrl"] })
    });
    };
    messageCreateModalForm();

// Delete-message
    function messageDeleteModalForm() {
     document.addEventListener('DOMContentLoaded', (e) => {
        var readDog = document.getElementsByClassName("message-delete");
        for (var index=0; index < readDog.length; index++) {
          modalForm(readDog[index], {formURL: readDog[index]["dataset"]["formUrl"]});
        }
      });
    };
    messageDeleteModalForm();


