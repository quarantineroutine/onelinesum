from typing import List
from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration


class Summarizer():
    def __init__(self):
        model_name = "quarantineroutine/distilkobart-rdrop-demo"

        tokenizer = PreTrainedTokenizerFast.from_pretrained(model_name)
        model = BartForConditionalGeneration.from_pretrained(model_name)
        model.eval()

        self.tokenizer = tokenizer
        self.model = model

    
    def summarize(self, conversations: List):
        max_length = 64
        num_beams = 5
        length_penalty = 1.2

        inputs = self.tokenizer("<s>" + "<sep>".join(conversations) + "</s>", return_tensors="pt")
        outputs = self.model.generate(
            inputs.input_ids,
            attention_mask=inputs.attention_mask,
            num_beams=num_beams,
            length_penalty=length_penalty,
            max_length=max_length,
            use_cache=True,
        )
        summarization = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return summarization
