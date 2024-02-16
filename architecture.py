from diagrams import Diagram, Cluster, Edge
from diagrams.generic.device import Tablet
from diagrams.generic.blank import Blank
from diagrams.saas.analytics import Snowflake
from diagrams.aws.storage import S3
from diagrams.custom import Custom

with Diagram("Architecture Diagram", show=False):
    website = Tablet("Website")
    
    with Cluster("Data Processing"):
        pdf = Custom("", "./asset/pdf_file.png")
        txt = Custom("txt", "./asset/txt-file.png")
        csv = Custom("CSV", "./asset/csv-file-format8052.jpg")

    with Cluster("Data Storage"):
        snowflake = Snowflake("Snowflake")
        s3 = S3("S3")
    
    website >> Edge(label="Scrape Data", color="brown") >> csv >> Edge(label="Stored it using SQlAlchemy", color="brown") >> snowflake
    pdf >> txt >> Edge(label="Storing it in s3", color="brown") >> s3
    pdf >> snowflake
        
