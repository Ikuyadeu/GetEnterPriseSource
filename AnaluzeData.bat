chcp 65001
for /f "skip=1 tokens=1,2* delims=," %%i in (projects.csv) do (
    python ./Contributors.py .\%%i %%j > Result\contoributor\%%j.txt
    python ./Issue_time.py .\%%i %%j > Result\issue\%%j.txt
    python ./PUlls.py .\%%i %%j > Result\pull\%%j.txt
)