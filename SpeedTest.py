from speedtest import Speedtest # pip install speedtest-cli
st = Speedtest()
print("Download: ", st.download() / 1024 / 1024)
print("Upload: ", st.upload() / 1024 / 1024)