# PyTest for rekindle.

Install **Python 3.9** (from microsoft store on Windows)

To conduct tests or write your own please download this repository to your machine and open as a project in PyCharm.
While opening it, please make sure you are working in virtualenv, to do not mess up with pure python installed on your machine.

Needed libraries from requirements.txt install after run project with virtualenv.

Update **config_template.json** file with correct data and save it as **config.json**

Logic to be used in tests should be placed in corresponding *utils* file.
After that you can start writing the tests in **tests/** directory remember to start the name of your file with **test\_\*.py**
it is needed by PyTest to recognize files to run with tests.
In the file create main class and under it create methods name convention is to use **test\_** at the beginning of each method,
thanks to this PyTest recognize each of these methods as separate test.

| File        | Description                                                                                                       |
|-------------|-------------------------------------------------------------------------------------------------------------------|
| utils_\*.py | Files with logic to be used in corresponding tests. Remember to import needed functions at the beginning of file. |
| config.json | File with configuration parameters shared across all tests.                                                       |

| Library     | Description                                                                                                                       |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------|
| PyTest      | Main library for framework. To run test there is need only to write *pytest* in the command line or *pytest path/to/test/file.py* |
| PyTest-HTML | Library to generate HTML reports to generate HTML report need put in command line *pytest --html=report.html*                     |
| requests    | Library to handle HTTPRequests                                                                                                    |
| psycopg2    | Library to handle database requests.                                                                                              |
| Faker       | Library to generate fake data.                                                                                                    |