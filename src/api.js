import PaLM from "palm-api";

let bot = new PaLM('AIzaSyDEPYNJqvyccJQ1AuXAxPfyx5Ic7IafQAs');

bot.generateText("Write a poem on puppies.", {
	temperature: 0.5,
	candidateCount: 1,
});

