# Información del challenge
data = {
    "name": "Claudio Mora",
    "mail": "kaelandres@gmail.com",
    "github_url": "https://github.com/kaelandres/challenge-LATAM-CM.git"
}

response = requests.post("https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer", json=data)


if response.status_code == 200:
    print("Challenge enviado exitosamente")
else:
    print(f"Error al enviar el challenge: {response.status_code}")
