import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json



def Scrap():
    Chosen_lang = input("Choose your Language (ex: en, fr, ar): ").strip()
    Chosen_Research = input("what do you want to research?: ").strip()

    url = f"https://{Chosen_lang}.wikipedia.org/wiki/{Chosen_Research}"

    page = requests.get(url)
    doc = BeautifulSoup(page.text, "html.parser")
    if page.status_code == 200:
        div_bodyContent = doc.find(class_="mw-content-ltr mw-parser-output")

        def Listing_links():
            def  has_wiki(href):
                return href and re.compile("wiki").search(href)

            href_Has_Wiki = div_bodyContent.find_all(href=has_wiki)

            #print(href_Has_Wiki[0].get("href"))
            href_info = [
                {"text":href.get_text(strip=True), "link":f"https://en.wikipedia.org{href.get('href')}"
            }
                for href in href_Has_Wiki
                if href.get_text(strip=True) and href.get("href").startswith("/wiki/") and not any(prefix in href.get("href") for prefix in ["/wiki/File:", "/wiki/Help:","/wiki/Special:","/wiki/Template","/wiki/List"])
            ]

            output_file = f"Links_from_{Chosen_Research}.csv"
            df =pd.DataFrame(href_info)
            df.drop_duplicates(subset="link", inplace=True)
            df.to_csv(output_file, index=False, header=False)
            print("Data successfully exported to", output_file)
        Listing_links()

        def Extract_content_table():    
            toc_container = doc.find(id="mw-panel-toc-list")
            h2_sections = toc_container.find_all("li",class_=re.compile("toc-level-1"))[1:]
            
            content_table = {}


            for section in h2_sections:
                h2_title_span = section.find("div",class_ = re.compile("toc-text")).find_all("span")[-1]
                if h2_title_span:
                    h2_title = h2_title_span.get_text(strip=True)
                else:
                    continue
                
                h3_titles = []
                h3_sections = section.find_all("li",class_=re.compile("toc-level-2"))
                for subsection in h3_sections:
                    h3_title_span = subsection.find("div",class_ = re.compile("toc-text")).find_all("span")[-1]
                    if h3_title_span:
                        h3_title = h3_title_span.get_text(strip=True)
                        h3_titles.append(h3_title)

                
                content_table[h2_title] = h3_titles

            """ print("Content Table Structure:",content_table)
            for h2, h3_list in content_table.items():
                print(f"\n{h2}:")
                for h3 in h3_list:
                    print(f"  - {h3}") """

            output_file_content_table = f"content_table_{Chosen_Research}.json"

            with open(output_file_content_table, "w", encoding="utf-8") as f:
                    json.dump(content_table, f, ensure_ascii=False, indent=2)
            print(f"\nContent table saved to {output_file_content_table}")
        Extract_content_table()

        def extract_articles_content():

            article_content = []
            current_h2 = None
            current_h2_dict = None
            current_h3 = None
            current_h3_dict = None

            elements = div_bodyContent.find_all(["h2","h3","p"])

            for element in elements:
                if element.name in ["h2","h3"]:
                    heading_text = element.get_text(strip=True)
                    if not heading_text:
                        continue
                    if element.name == "h2":
                        if current_h2_dict is not None:
                            if current_h3_dict is not None:
                                current_h2_dict["subsection"].append(current_h3_dict)
                                current_h3_dict = None
                            article_content.append(current_h2_dict)
                            
                        current_h2 = heading_text
                        current_h2_dict ={
                            "h2": f"{current_h2}",
                            "paragraph_text": [],
                            "subsection":[]
                        }
                        current_h3 = None
                        current_h3_dict = None

                    elif element.name == "h3":
                        if current_h3_dict is not None:
                            current_h2_dict["subsection"].append(current_h3_dict)
                        
                        current_h3 = heading_text
                        current_h3_dict = {
                            "h3":f"{current_h3}",
                            "paragraph_text":[]
                        }

                elif element.name == "p":
                    paragraph_text = element.get_text(strip =True)
                    if paragraph_text:
                        if current_h2_dict is None:
                            current_h2_dict = {
                                "h2":"Introduction",
                                "paragraph_text": [paragraph_text],
                                "subsection":[]
                            }
                        elif current_h3_dict is not None:
                            current_h3_dict["paragraph_text"].append(paragraph_text)
                        else: 
                            current_h2_dict["paragraph_text"].append(paragraph_text)

            if current_h2_dict is not None:
                if current_h3_dict is not None:
                    current_h2_dict["subsections"].append(current_h3_dict)
                article_content.append(current_h2_dict)

            output_file_Article_content = f"article_content_{Chosen_Research}.json" 
            with open(output_file_Article_content, "w", encoding="utf-8") as f:
                json.dump(article_content, f, ensure_ascii=False, indent=2)
                print(f"\nContent table saved to {output_file_Article_content}")
        extract_articles_content()

    else:
        print("Error")


if __name__ == "__main__":
    Scrap()