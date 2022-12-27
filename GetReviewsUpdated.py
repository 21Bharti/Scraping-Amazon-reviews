from bs4 import BeautifulSoup
from requests_html import HTMLSession
import os

def getReviews(Page_No):
    Base_URL = "https://www.mouthshut.com"
    Page = Base_URL + "/product-reviews/Amazon-in-reviews-925670774-page-" + str(Page_No)

    Reviews_Folder = "ReviewsPage10Pages/"
    if not os.path.exists(Reviews_Folder):
        os.mkdir(Reviews_Folder)

    s = HTMLSession()
    response = s.get(Page)
    response.html.render(timeout=20)

    soup = BeautifulSoup(response.html.html, "html.parser")
    review_divs = soup.find_all("div", {"class": "row review-article"})
    print("Total Reviews :", len(review_divs))

    for div in review_divs:
        Name = div.find("div", {"class": "user-ms-name"}).text
        review_data = div.find("div", {"class": "more reviewdata"})
        review = review_data.text
        with open(Reviews_Folder + Name + ".txt", "w", encoding="utf-8") as f:
            f.write(review)

    # print(Reviews)
    print("Document Extraction Completed")

if __name__ == "__main__":
    # Pass the Page Number as an Argument
    for k in range(10):
        getReviews(Page_No=k+1)