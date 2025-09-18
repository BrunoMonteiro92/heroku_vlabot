import { Telegraf } from "telegraf";
import fs from "fs";
import path from "path";
import dotenv from "dotenv";
import { logCommand, logSending, randomChoice } from "./utils.js";

dotenv.config();

const imageQueue: string[] = [];
const soundQueue: string[] = [];
const MAX_IMAGE = 20;
const MAX_SOUND = 5;

const imagesDir = "./images";
const soundsDir = "./sound";

const pics = fs.readdirSync(imagesDir);
const audios = fs.readdirSync(soundsDir);

const TOKEN = process.env.TELEGRAM_TOKEN!;
if (!TOKEN) {
  console.error("TELEGRAM_TOKEN is not set in environment variables!");
  process.exit(1);
}

const response: string[] = [
  "Gua",
  "Beisso aí",
  "Risos",
  "Hausha7hausua7e",
  "Calma",
  "Te fode carlos",
  "Nossa",
  "Você tá bem, cara?",
  "Uia",
  "Te fode carlos",
  ".",
  "Egua",
  "Nao ma",
  "Bacana",
  "Essa fera",
  "Que loucura",
  "Te fode carlos",
  "O loco Bichow",
  "Tenso",
  "Diz",
  "Rs",
  "E foi indo e foi indo... E tamo aqui agora",
  "Meu nome é Vladimir Lima tenho 24 anos, faço cerveja, ando de bicicleta e só",
  "Complicado esse humor",
  "boa",
  "Esse tempo todo?",
  "Vai fumar maconha ma\nQue tu fica de boas\nMenos exaltado",
  "Bebam água",
  "Opa",
  "Ma",
  "Huum",
  "Huuum",
  "Pera",
  "Tô com sono",
  "Bacana, bacana",
];

const responseAsk: string[] = [
  "Calma, explica aí q eu não entendi",
  "Q?",
  "Depende",
  "Não sei, foda-se",
  "Que pergunta bosta, em? Vai se fuder",
  "Não, te fode",
  "Provavelmente nao em...",
  "Olha, eu acho que sim em...",
  "Dificil isso...",
  "Olha, talvez",
  "Sim! AEAEAEAEA!",
  "Peraí que eu to comendo",
  "Café?",
  "Que o q ma",
  "Não sei ma",
  "Hein?",
  "É",
];

const bot: Telegraf = new Telegraf(TOKEN);

// /help
bot.command("help", (context) => {
  context.replyWithMarkdownV2(
    "*Vlad Bot v6.0*\n\n" +
      "*/vlad* - comentário\n" +
      "*/askvlad* - respostas\n" +
      "*/fera* - fotos\n" +
      "*/calma* - calma\n" +
      "*/diz* - áudios\n\n" +
      "*Desenvolvido por:* Yuri Reis / Bruno Monteiro"
  );
});

// /calma
bot.command("calma", async (context) => {
  logCommand(context.chat.id, "/calma");

  const file = Math.random() < 0.5 ? "./calma.jpg" : "./calma2.jpg";
  logSending(context.chat.id, file);
  await context.replyWithPhoto({ source: file });
});

// /vlad
bot.command("vlad", (context) => {
  logCommand(context.chat.id, "/vlad");

  let op = randomChoice(response);
  if (op.includes("Te fode carlos")) {
    const firstName = context.from?.first_name || "Carlos";
    op = op.replace("carlos", firstName.split(" ")[0]!);
  }

  logSending(context.chat.id, op);

  context.reply(op);
});

// /fera
bot.command("fera", async (context) => {
  logCommand(context.chat.id, "/fera");

  let img = randomChoice(pics);
  while (imageQueue.includes(img)) {
    img = randomChoice(pics);
  }
  imageQueue.push(img);
  if (imageQueue.length > MAX_IMAGE) imageQueue.shift();

  logSending(context.chat.id, img);

  if (img.endsWith(".gif")) {
    await context.replyWithDocument({ source: path.join(imagesDir, img) });
  } else {
    await context.replyWithPhoto({ source: path.join(imagesDir, img) });
  }
});

// /askvlad
bot.command("askvlad", (context) => {
  logCommand(context.chat.id, "/askvlad");

  const parts = context.message.text.split(" ");
  if (parts.length === 1) {
    context.reply("Algo de errado não está certo, cadê a pergunta?", {
      reply_parameters: { message_id: context.message.message_id },
    });
  } else {
    const op = randomChoice(responseAsk);

    logSending(context.chat.id, op);
    context.reply(op, {
      reply_parameters: { message_id: context.message.message_id },
    });
  }
});

// /diz
bot.command("diz", async (context) => {
  logCommand(context.chat.id, "/diz");

  let aud = randomChoice(audios);
  while (soundQueue.includes(aud)) {
    aud = randomChoice(audios);
  }
  soundQueue.push(aud);
  if (soundQueue.length > MAX_SOUND) soundQueue.shift();

  logSending(context.chat.id, aud);

  await context.replyWithVoice({ source: path.join(soundsDir, aud) });
});

// top
bot.hears(/\btop[^ao]*\b/i, (context) => {
  logCommand(context.chat.id, "TOP");
  logSending(context.chat.id, "Não diga top, diga xibata");

  context.reply("Não diga top, diga xibata", {
    reply_parameters: { message_id: context.message.message_id },
  });
});

// alô
bot.hears(/\ba+l[oô]+\b/iu, (context) => {
  logCommand(context.chat.id, "ALÔ");

  const match = context.message.text.match(/\ba+l[oô]+\b/i);

  logSending(context.chat.id, "Não diga alô, diga: Essa fera aí!");
  context.reply(`Não diga ${match?.[0]}, diga: Essa fera aí!`, {
    reply_parameters: { message_id: context.message.message_id },
  });
});

bot.launch();
console.log("Vlad bot is running...");

process.once("SIGINT", () => bot.stop("SIGINT"));
process.once("SIGTERM", () => bot.stop("SIGTERM"));
