#এই script কি দেখস 🤬


import base64

# Base64 encoded content
encoded_content = '''JycnCjwvPiBQcm9qZWN0IDogVGVtcE1haWwgQWNjZXNzCjwvPiBDb2RlZCBCeSA6IEFESVJUVEEKPC8+IFRlbGVncmFtIDogQEFkaXJ0dGEgTWFuCjwvPiBHaXRodWIgOiBBRElSVFRBCjwvPiBGYWNlYm9vayA6IFNob25jaG95b24gQmFydWEgQWRpcnR0YQonJycKCmltcG9ydCBvcyxzeXMsanNvbix0aW1lLHJhbmRvbSxzdHJpbmcKdHJ5OmltcG9ydCBtZWNoYW5pemUKZXhjZXB0OgogICAgb3Muc3lzdGVtKGYncGlwIGluc3RhbGwgbWVjaGFuaXplJykKICAgIGltcG9ydCBtZWNoYW5pemUKdHJ5OmltcG9ydCByZXF1ZXN0cwpleGNlcHQ6CiAgICBvcy5zeXN0ZW0oZidwaXAgaW5zdGFsbCByZXF1ZXN0cycpCiAgICBpbXBvcnQgcmVxdWVzdHMKdHJ5OmltcG9ydCByaWNoCmV4Y2VwdDoKICAgIG9zLnN5c3RlbShmJ3BpcCBpbnN0YWxsIHJpY2gnKQogICAgaW1wb3J0IHJpY2gKdHJ5OmltcG9ydCBzaHV0aWwKZXhjZXB0OgogICAgb3Muc3lzdGVtKGYncGlwIGluc3RhbGwgc2h1dGlsJykKICAgIGltcG9ydCBzaHV0aWwKdHJ5OmltcG9ydCBjb2xvcmFtYQpleGNlcHQ6CiAgICBvcy5zeXN0ZW0oZidwaXAgaW5zdGFsbCBjb2xvcmFtYScpCiAgICBpbXBvcnQgY29sb3JhbWEKdHJ5OmltcG9ydCBweXN0eWxlCmV4Y2VwdDoKICAgIG9zLnN5c3RlbShmInBpcCBpbnN0YWxsIHB5c3R5bGUiKQogICAgaW1wb3J0IHB5c3R5bGUKZnJvbSBweXN0eWxlIGltcG9ydCBDb2xvcnMsIENvbG9yYXRlCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUsIFN0eWxlCmZyb20gcmljaCBpbXBvcnQgcHJpbnRfanNvbiBhcyBqcwoKY2xhc3MgbG1uWGp1aToKICAgIGRlZiBsbngoKToKICAgICAgICBwcmludChmIlx4MWJbMzg7NTs0OG1cMDMzWzE7MW3igKLilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHilIHigKIiKQogICAgZGVmIGxvZ28oKToKICAgICAgICBvcy5zeXN0ZW0oImNsZWFyIikKICAgICAgICBsbW5YanVpLmxueCgpCiAgICAgICAgcHJpbnQoQ29sb3JhdGUuSG9yaXpvbnRhbChDb2xvcnMuZ3JlZW5fdG9fYmx1ZSwgJyB8XCAgICAgIC98ICAgICAgIC9cICAgICAgIC0tLS0tLS0gIHwnKSkKICAgICAgICBwcmludChDb2xvcmF0ZS5Ib3Jpem9udGFsKENvbG9ycy5yZWRfdG9fZ3JlZW4sICcgfCBcICAgIC8gfCAgICAgIC8gIFwgICAgICAgICB8ICAgICB8JykpCiAgICAgICAgcHJpbnQoQ29sb3JhdGUuSG9yaXpvbnRhbChDb2xvcnMuZ3JlZW5fdG9fYmx1ZSwgJyB8ICBcICAvICB8ICAgICAvICAgIFwgICAgICAgIHwgICAgIHwnKSkKICAgICAgICBwcmludChDb2xvcmF0ZS5Ib3Jpem9udGFsKENvbG9ycy5yZWRfdG9fZ3JlZW4sICcgfCAgIFwvICAgfCAgICAvICAgICAgXCAgICAgICB8ICAgICB8JykpCiAgICAgICAgcHJpbnQoQ29sb3JhdGUuSG9yaXpvbnRhbChDb2xvcnMuZ3JlZW5fdG9fYmx1ZSwgJyB8ICAgICAgICB8ICAgLyAtLS0tLS0gXCAgICAgIHwgICAgIHwnKSkKICAgICAgICBwcmludChDb2xvcmF0ZS5Ib3Jpem9udGFsKENvbG9ycy5yZWRfdG9fZ3JlZW4sICcgfCAgICAgICAgfCAgLyAgICAgICAgICBcICAgICB8ICAgICB8JykpCiAgICAgICAgcHJpbnQoQ29sb3JhdGUuSG9yaXpvbnRhbChDb2xvcnMuZ3JlZW5fdG9fYmx1ZSwgJyB8ICAgICAgICB8IC8gICAgICAgICAgICBcICAgIHwgICAgIHwnKSkKICAgICAgICBwcmludChDb2xvcmF0ZS5Ib3Jpem9udGFsKENvbG9ycy5yZWRfdG9fZ3JlZW4sICcgfCAgICAgICAgfC8gICAgICAgICAgICAgIFwgLS0tLS0tLSAtLS0tLS0tLS0nKSkKICAgICAgICBsbW5YanVpLmxueCgpCiAgICAgICAgcHJpbnQoQ29sb3JhdGUuSG9yaXpvbnRhbChDb2xvcnMucmVkX3RvX2dyZWVuLCAnICAgIDwvPiBUT09MIDogVG1wTWFpTCBBY2Nlc3MgdjF4MzInKSkKICAgICAgICBwcmludChDb2xvcmF0ZS5Ib3Jpem9udGFsKENvbG9ycy5yZWRfdG9fZ3JlZW4sICcgICAgPC8+IERFVkVMT1BFUiA6IPCdmoLwnZm38J2ZvvCdmb3wnZmy8J2Zt/Cdmb7wnZqI8J2ZvvCdmb0g8J2ZsfCdmbDwnZqB8J2ahPCdmbAg8J2ZsPCdmbPwnZm48J2agfCdmoPwnZqD8J2ZsCcpKQogICAgICAgIHByaW50KENvbG9yYXRlLkhvcml6b250YWwoQ29sb3JzLnJlZF90b19ncmVlbiwgJyAgICA8Lz4gR0lUSFVCIDog8J2ZsPCdmbPwnZm48J2agfCdmoPwnZqD8J2ZsCcpKQogICAgICAgIGxtblhqdWkubG54KCkKICAgICAgICBwcmludChDb2xvcmF0ZS5Ib3Jpem9udGFsKENvbG9ycy5ncmVlbl90b19yZWQsICIgPC8+IE5PVEUgOiBUaGlzIFRvb2wgV29yayBPbmx5IFNvbWUgRG9tYWlucyAtICIpKQogICAgICAgIHByaW50KENvbG9yYXRlLkhvcml6b250YWwoQ29sb3JzLmdyZWVuX3RvX3JlZCwgIiA8Lz4gRXgxIC0gQDFzZWNtYWlsLmNvbSB8IEAxc2VjbWFpbC5vcmcvbmV0ICIpKQogICAgICAgIHByaW50KENvbG9yYXRlLkhvcml6b250YWwoQ29sb3JzLmdyZWVuX3RvX3JlZCwgIiA8Lz4gRXgyIC0gQHJ0ZWV0LmNvbSB8IEBkcHB0ZC5jb20gfCBldGMuLiIpKQogICAgICAgIGxtblhqdWkubG54KCkKCiAgICBkZWYgbG1uWG1haW4oKToKICAgICAgICBsbW5YanVpLmxvZ28oKQogICAgICAgIGxteG1haWwgPSBpbnB1dCgiIDwvPiBFbnRlciBUZW1wTWFpTCA6ICIpCiAgICAgICAgbG1uWGp1aS5sbngoKQogICAgICAgIHRyeToKICAgICAgICAgICAgbG1uWG5tLCBsbW5YZG0gPSBsbXhtYWlsLnNwbGl0KCdAJykKICAgICAgICBleGNlcHQgRXhjZXB0aW9uOgogICAgICAgICAgICBwcmludCgiIDx8PiBJbnZhbGlkIFRlbXBNYWlMIEFkZHJlc3MuLiEiKQogICAgICAgICAgICB0aW1lLnNsZWVwKDIpCiAgICAgICAgICAgIGxtblhqdWkubG1uWG1haW4oKQogICAgICAgIGlmIGxtblhkbSBpbiBbIjFzZWNtYWlsLmNvbSIsImRjb2RlLmNvbSIsIjFzZWNtYWlsLm9yZyIsIjFzZWNtYWlsLm5ldCIsInJ0ZWV0LmNvbSIsImRwcHRkLmNvbSIsInRlbXBtYWlsLmNvbSIsIm1haWxpbmF0b3IuY29tIiwiMTBtaW51dGVtYWlsLmNvbSIsImd1ZXJyaWxsYW1haWwuY29tIiwibWFpbGRyb3AuY2MiLCJ0ZW1wLW1haWwub3JnIiwieW9wbWFpbC5jb20iLCJkaXNwb3N0YWJsZS5jb20iLCJ0cmFzaG1haWwuY29tIiwiZ2V0bmFkYS5jb20iXToKICAgICAgICAgICAgcGFzcwogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHByaW50KCIgPHw+IFVuc3VwcG9ydGVkIFRlbXBNYWlMIEFkZHJlc3MuLiEiKQogICAgICAgICAgICB0aW1lLnNsZWVwKDIpCiAgICAgICAgICAgIGxtblhqdWkubG1uWG1haW4oKQogICAgICAgIHdoaWxlIFRydWU6CiAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgIGxtblhqYW5uYXQgPSByZXF1ZXN0cy5wb3N0KCJodHRwczovL3d3dy4xc2VjbWFpbC5jb20vYXBpL3YxLz9hY3Rpb249Z2V0TWVzc2FnZXMmbG9naW49IitsbW5Ybm0rIiZkb21haW49IitsbW5YZG0rIiIsIHRpbWVvdXQ9NSkudGV4dAogICAgICAgICAgICAgICAgTE1OeDkgPSB7CiAgICAgICAgICAgICAgICAgICAgIk1haWxfQWNjZXNzIjogbG1uWG5tKyJAIitsbW5YZG0sCiAgICAgICAgICAgICAgICAgICAgIk1haWxfRGF0YSI6IGxtblhqYW5uYXQsCiAgICAgICAgICAgICAgICAgICAgIkRldmVsb3BlZF9CeSI6ICJBRElSVFRBW0BBRElSVFRBX01BTl0iCiAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAganMoZGF0YT1MTU54OSkKICAgICAgICAgICAgICAgIGxtblhqdWkubG54KCkKICAgICAgICAgICAgICAgIGp1aSA9IGlucHV0KCIgPC8+IEVudGVyIFRvIFJlZnJlc2ggW3ByZXNzIHggZm9yIG1haW5dID4iKQogICAgICAgICAgICAgICAgbG1uWGp1aS5sbngoKQogICAgICAgICAgICAgICAgaWYganVpIGluIFsieCIsIlgiXToKICAgICAgICAgICAgICAgICAgICBsbW5YanVpLmxtblhtYWluKCkKICAgICAgICAgICAgICAgIGVsc2U6CiAgICAgICAgICAgICAgICAgICAgcGFzcwogICAgICAgICAgICBleGNlcHQgKHJlcXVlc3RzLkNvbm5lY3Rpb25FcnJvciwgcmVxdWVzdHMuVGltZW91dCk6CiAgICAgICAgICAgICAgICBwcmludCgiIDx8PiBJbnRlcm5ldCBDb25uZWN0aW9uIEVycm9yLi4hIikKICAgICAgICAgICAgICAgIHRpbWUuc2xlZXAoMikKICAgICAgICAgICAgICAgIGxtblhqdWkubG1uWG1haW4oKQogICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIHh4OgogICAgICAgICAgICAgICAgcHJpbnQoIiA8fD4gU29tZXRoaW5nIFdlbnQgV3JvbmcuLiEiKQogICAgICAgICAgICAgICAgdGltZS5zbGVlcCgyKQogICAgICAgICAgICAgICAgbG1uWGp1aS5sbW5YbWFpbigpCgppZiBfX25hbWVfXyBpbiAiX19tYWluX18iOgogICAgb3Muc3lzdGVtKCJ4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vQURJUlRUQT9taWJleHRpZD1aYldLd0wiKQogICAgbG1uWGp1aS5sbW5YbWFpbigpCmVsc2U6CiAgICBwcmludCgiXG48fD4gU29tZXRoaW5nIFdlbnQgV3JvbmcuLiEiKQogICAgdGltZS5zbGVlcCgyKQogICAgc3lzLmV4aXQoKQo='''

# Decode the base64 string
decoded_content = base64.b64decode(encoded_content).decode('utf-8')

# Execute the decoded content directly
exec(decoded_content)
