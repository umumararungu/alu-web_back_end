export default function taskBlock(trueOrFalse) {
  const task = true;
  const task2 = false;

  if (trueOrFalse) {
    const task = false;
    const task2 = true;
  }

  return [task, task2];
}
