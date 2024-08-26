# TODO: refactor this cell so that there is no error occuring
from dotenv import load_dotenv
load_dotenv()
if not os.path.isdir('/content/drive/MyDrive/MADS2400/Google-Recaptcha-V2-Images') or not os.path.isdir('Google-Recaptcha-V2-Images'):
  git_fine_grained_token = os.environ["git_fine_grained_token"]
  username = 'RaresMihai11'
  repository = 'Google-Recaptcha-V2-Images'
  !git clone https://{git_fine_grained_token}@github.com/{username}/{repository}
else:
  logger.info("already cloned image repository")