export default function taskBlock(trueOrFalse) {
  task = false;
  task2 = true;

  if (trueOrFalse) {
    task = true;
    task2 = false;
  }
  var task;
  var task2;
  return [task, task2];
}
