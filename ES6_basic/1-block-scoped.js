export default function taskBlock(trueOrFalse) {
  task = false;
  task2 = true;

  if (trueOrFalse) {
    task = false;
    task2 = true;
  }
  var task;
  var task2;
  return [task, task2];
}
