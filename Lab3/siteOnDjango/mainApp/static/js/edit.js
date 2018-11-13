$('#edit').click(function(){
  $('#edit').attr("disabled", "true");;
  var eventId = $('#eventId').text();
  console.log(eventId);
  var title = $('#title').text();
  var date = $('#date').text();
  var description = $('#description').text();
  console.log(title + " " + date + "   " +  description);
  $('#title').remove();
  $('#date').remove();
  $('#description').remove();
  date = date.split("-");
  console.log(date);


  $('#mainForm').append($('<input>',{type:"text", name:"title", placeholder:"Name", value:title}));
  $('#mainForm').append($('<input>',{type:"date", name:"date", value:date[2] + "-" + date[1] + "-" + date[0]}));
  $('#mainForm').append($('<textarea/>',{name:"description", rows: 3,  placeholder:"Description", text: description}));
  $('#mainForm').append($('<button/>',{id: "saveEdit", class: "btn btn-primary outline-none",text: "Підтвердити", type: "submit"}));


})
