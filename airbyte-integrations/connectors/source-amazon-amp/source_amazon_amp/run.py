import sys
from airbyte_cdk.entrypoint import launch
#from .source import SourceAmazonAmp
from source_amazon_amp.source_amazon_amp import SourceAmazonAMP

def run():
    source = SourceAmazonAMP()
    launch(source, sys.argv[1:])

if __name__ == "__main__":
    run()
