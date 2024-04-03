def cleanup(url, player):
    for script in soup(["script", "style"]):
        script.decompose()    

    with open('output_file.txt', "w") as text_file:
        text_file.write("\nURL : "+ url)
        text_file.write("\nTitle : " + player)
        
                
        for p_tag_data in soup.find_all('p'):
            text_file.write("\n"+p_tag_data.text)
            
        for li_tag_data in soup.find_all('li'):
            text_file.write("\n"+li_tag_data.text)
            
        for div_tag_data in soup.find_all('div'):
            text_file.write("\n"+div_tag_data.text)