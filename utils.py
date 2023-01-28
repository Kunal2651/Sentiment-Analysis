import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode("utf-8")
    #binary data of image
    # print(graph)
    buffer.close()
    return graph

def get_plot(data , labels,autopct="%0.1f%%",startangle=90):

    plt.switch_backend("AGG")
    plt.figure(figsize=(10,5))
    plt.axis('equal')
    plt.title('Sentiment Analysis')
    plt.pie(data,labels=labels,autopct=autopct,startangle=startangle)
    plt.tight_layout()

    graph = get_graph()


    # value=[wpositive,positive,wnegative,negative,neutral]
    # labels=['Weakly Positive','Positive','Weakly Negative','Negative','Neutral']
    # plt.axis('equal')
    # plt.pie(value,labels=labels,autopct='%0.1f%%',startangle=90)
    # plt.title('Sentiment Analysis')
    # plt.tight_layout()
    # plt.show()

    return graph