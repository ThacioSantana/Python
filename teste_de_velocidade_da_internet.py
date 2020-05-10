import speedtest

st = speedtest.speedtest()
print('Download speed: {}'.format(st.download()))
print('Upload speed: {}'.format(st.upload()))