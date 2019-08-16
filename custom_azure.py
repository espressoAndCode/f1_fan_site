from storages.backends.azure_storage import AzureStorage
import os

class AzureStaticStorage(AzureStorage):
    account_name = 'f1fanatic' # Must be replaced by your storage_account_name
    account_key = os.environ['STORAGE_ACCT_KEY']
    azure_container = 'static'
    expiration_secs = None
