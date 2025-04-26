
import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="Threat Intelligence Extractor (Lite)", layout="wide")
st.title("Threat Intelligence Extractor (Lite)")
st.markdown("Paste text from threat reports or incident blogs to extract IOCs using pure regex.")

# IOC Patterns
ioc_patterns = {
    "IP Address": r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",
    "Domain": r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b",
    "MD5 Hash": r"\b[a-fA-F0-9]{32}\b",
    "SHA1 Hash": r"\b[a-fA-F0-9]{40}\b",
    "SHA256 Hash": r"\b[a-fA-F0-9]{64}\b"
}

sample_text = '''APT28 used domain mail-login[.]co targeting Ukraine.
The malicious file had an MD5 hash of 5d41402abc4b2a76b9719d911017c592 and connected to IP 185.100.87.72 via cc[.]malicious-domain[.]org.'''

text_input = st.text_area("Paste threat report text:", sample_text, height=250)

if st.button("Extract IOCs"):
    if not text_input.strip():
        st.warning("Please paste some threat text.")
    else:
        results = []
        for label, pattern in ioc_patterns.items():
            matches = re.findall(pattern, text_input)
            for match in matches:
                results.append((match, label))
        
        if results:
            df = pd.DataFrame(results, columns=["Match", "Type"])
            st.dataframe(df)
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("Download Results as CSV", data=csv, file_name="extracted_iocs.csv", mime="text/csv")
        else:
            st.info("No IOCs detected.")
