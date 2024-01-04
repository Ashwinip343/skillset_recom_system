import PaLM from "palm-api";

let bot = new PaLM('YOUR_API_KEY');

bot.generateText("Write a poem on puppies.", {
	temperature: 0.5,
	candidateCount: 1,
});

