import os
import google.generativeai as genai

# Autenticação
import json
import tempfile

# Salva o JSON temporariamente
with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp:
    temp.write(os.environ['GOOGLE_APPLICATION_CREDENTIALS_JSON'])
    temp.flush()
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = temp.name

# Inicializa a API Gemini
genai.configure(api_key=None)

for m in genai.list_models():
    print(m.name, "-", m.supported_generation_methods)

model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# Lê o diff da PR
diff_output = os.popen("git diff --diff-filter=AMR --name-only HEAD~1 HEAD").read()

# Envia o diff para análise
response = model.generate_content(f"Faça uma revisão de código no seguinte diff:\n\n{diff_output}")

# Exibe resposta
print(response.text)

