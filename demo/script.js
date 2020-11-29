$(function () {
  move(0);
  $('#left').on('click', function () {
    move(-1);
  })
  $('#right').on('click', function () {
    move(1);
  })
});