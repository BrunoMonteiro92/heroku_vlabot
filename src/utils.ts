function logCommand(chatId: number, command: string): void {
  const now = new Date().toLocaleString();
  console.log(`[${now}] Command "${command}" received from chat ${chatId}`);
}

function logSending(chatId: number, content: string): void {
  const now = new Date().toLocaleString();
  console.log(`[${now}] Sending "${content}" to chat ${chatId}`);
}

function randomChoice<T>(arr: T[]): T {
  return arr[Math.floor(Math.random() * arr.length)]!;
}

export { logCommand, logSending, randomChoice };
