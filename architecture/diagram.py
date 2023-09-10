from diagrams import Diagram
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL

with Diagram(name="local_library_website with On-Premise", show=False):    
    Server("Django development server") >> PostgreSQL("main")