# University Information Extractor
Welcome to University Information Extractor! 🎓 This Python script provides functionalities to extract and analyze data about universities worldwide, offering insights into international rankings, national standings, and more.

## About
This script processes information from two CSV files: `TopUni.csv`, containing university rankings, and `capitals.csv`, containing data about capital cities and their respective countries. It offers a comprehensive analysis of universities based on their rankings and geographical locations.

## Features
- **Total Universities Count**: Get the total number of universities listed in the ranking.
- **Available Countries**: Retrieve a list of available countries for which university rankings are provided.
- **Available Continents**: Obtain a list of available continents based on the countries listed in the capital cities dataset.
- **University International Rank**: Find the international rank and name of a university based on a specific country.
- **University National Rank**: Determine the national rank and name of a university based on a specific country.
- **Average Score**: Calculate the average score of universities in a particular country.
- **Relative Score**: Compute the relative score of universities compared to the top university in the same continent.
- **Capital City**: Get the capital city of a specific country.
- **Universities Holding Capital Name**: Find universities that contain the name of the capital city.

## Requirements
- Python 3.x
- pandas library

## Usage
1. Ensure you have the required CSV files: `TopUni.csv` and `capitals.csv`.
2. Run the `getInformation` function in `univRanking.py`, providing the desired country, the filename for university rankings (`TopUni.csv`), and the filename for the capitals dataset (`capitals.csv`).
3. The script will generate an `output.txt` file containing the extracted information.

## Example
```python
from univRanking import getInformation

# Extract information for the USA
getInformation("USA", 'TopUni.csv', 'capitals.csv')
```

## Output
The extracted information will be written to the `output.txt` file in the following format:

```
Total number of universities => 1000
Available countries => COUNTRY1, COUNTRY2, ...
Available continents => CONTINENT1, CONTINENT2, ...
At international rank => RANK the university name is => UNIVERSITY_NAME
At national rank => RANK the university name is => UNIVERSITY_NAME
The average score => AVERAGE_SCORE%
The relative score to the top university in CONTINENT_NAME is => AVERAGE_SCORE/HIGHEST_SCORE x 100% = RELATIVE_SCORE%
The capital is => CAPITAL_NAME
The universities that contain the capital name => 
    #1 UNIVERSITY_NAME1
    #2 UNIVERSITY_NAME2
    ...
```


## Adding or Modifying Data

### Adding New University Rankings
To add new university rankings to the dataset:

1. Open the `TopUni.csv` file in a text editor or spreadsheet software.
2. Append the new university data following the same format as existing entries:
   - Ensure each row represents a single university with relevant columns for ranking, university name, country, etc.
   - Save the file after adding the new data.

### Modifying Capital City Information
To modify capital city information in the dataset:

1. Open the `capitals.csv` file in a text editor or spreadsheet software.
2. Locate the entry corresponding to the country whose capital city information you want to modify.
3. Edit the relevant fields such as the capital city name, country name, etc.
4. Save the file after making the modifications.

### Guidelines
- Maintain consistency in data formatting and naming conventions.
- Create backups of the original CSV files before making any modifications.
- Verify the accuracy of added or modified data by cross-referencing with reliable sources

## Contributing
Contributions to University Information Extractor are welcome! Whether you're adding new features, improving existing functionalities, or fixing bugs, your contributions are valuable. Please refer to the [contributing guidelines](CONTRIBUTING.md) for more information.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions regarding University Information Extractor, feel free to reach out.

Happy analyzing! 🎓✨
