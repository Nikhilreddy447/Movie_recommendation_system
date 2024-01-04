movies_link = "https://drive.google.com/file/d/1n4tgU_rZqJsGrAuptWo1znmJ78QMWClB/uc?export=download"
similarity_link = "https://drive.google.com/file/d/12B1D8sSZk_ddDeMdhR_jlVmHuXpmunXP/uc?export=download"

import requests

response_movies = requests.get(movies_link)
response_similarity = requests.get(similarity_link)

with open("movies.pkl", "wb") as f:
    f.write(response_movies.content)
    
with open("similarity.pkl","wb") as f:
    f.write(response_similarity.content)