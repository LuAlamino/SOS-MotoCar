from transformers import GPT2LMHeadModel, GPT2Tokenizer

def get_mecanico_ai_bio(name_fantasy, cidade):
    tokenizer = GPT2Tokenizer.from_pretrained('pierreguillou/gpt2-small-portuguese')
    model = GPT2LMHeadModel.from_pretrained('pierreguillou/gpt2-small-portuguese')

    prompt = f"{name_fantasy} é uma Otima Mecânica localizada em {cidade} ."

    inputs = tokenizer.encode(prompt, return_tensors='pt')

    # Gerar a resposta
    output = model.generate(
        inputs,
        max_length=30,  # Limitar o comprimento para evitar respostas longas
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        early_stopping=True,
        pad_token_id=tokenizer.eos_token_id  # Usar o token de fim de sequência para evitar texto extra
    )

    # Decodificar e retornar a resposta
    result = tokenizer.decode(output[0], skip_special_tokens=True).strip()

    # Garantir que apenas o elogio seja retornado
    return result.split("\n")[0].strip()


def get_car_ai_bio(model_name, brand, year):
    # Carregar o modelo e o tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained('pierreguillou/gpt2-small-portuguese')
    model = GPT2LMHeadModel.from_pretrained('pierreguillou/gpt2-small-portuguese')

    # Preparar o prompt
    prompt = f"Descreva especificações técnicas apenas sobre o carro {brand} {model_name}  em apenas 250 caracteres."

    # Tokenizar o prompt
    inputs = tokenizer.encode(prompt, return_tensors='pt')

    # Gerar a resposta
    output = model.generate(
        inputs,
        max_length=300,  # Ajustar o comprimento se necessário
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        early_stopping=True
    )

    # Decodificar e retornar a resposta
    result = tokenizer.decode(output[0], skip_special_tokens=True)

    # Limitar a 250 caracteres e remover o prompt da resposta
    start_idx = len(prompt)
    return result[start_idx:].strip()[:250]


