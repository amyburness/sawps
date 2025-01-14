import React, { useEffect, useState } from "react";
import { Bar } from 'react-chartjs-2';
import axios from "axios";
import { Grid } from "@mui/material";
import Loading from "../../../components/Loading";

const FETCH_SPECIES_DENSITY = "/api/properties-per-population-category/";

const availableColors = [
  'rgba(112, 178, 118, 1)',
  'rgba(250, 167, 85, 1)',
  'rgba(157, 133, 190, 1)',
  '#FF5252',
  '#616161',
  'rgba(112, 178, 118, 0.5)',
  'rgba(250, 167, 85, 0.5)',
  'rgba(157, 133, 190, 0.5)',
  'rgba(255, 82, 82, 0.5)',
  'rgba(97, 97, 97, 0.5)'
];

function processChartData(input: any) {
    const datasets = [];

    if (typeof input === 'undefined' || typeof  input.years === 'undefined') {
        return {
            labels: [],
            datasets: []
        };
    }

    let colorIndex = 0;

    for (const year of input.years) {
        const dataset = {
            label: year.toString(),
            // @ts-ignore
            data: [],
            backgroundColor: availableColors[colorIndex],
            skipNull: true
        };

        for (const category of input.category_labels) {
            const entry = input.data.find((e: any) => e.year === year && e.category === category);
            dataset.data.push(entry && entry.property_count ? entry.property_count : null);
        }
        datasets.push(dataset);
        colorIndex = (colorIndex + 1) % availableColors.length;
    }

    return {
        labels: input.category_labels,
        datasets: datasets.sort((a, b) => parseInt(a.label) - parseInt(b.label))
    };
}

const PopulationCategoryChart = (props: any) => {
    const {
      selectedSpecies,
      propertyId,
      startYear,
      endYear,
      onEmptyDatasets
    } = props;

    const [loading, setLoading] = useState<boolean>(false);
    const [populationData, setPopulationData] = useState([]);
    const apiUrl = `${FETCH_SPECIES_DENSITY}?start_year=${startYear}&end_year=${endYear}&species=${selectedSpecies}&property=${propertyId}`;

    const fetchPopulationCategoryData = () => {
      setLoading(true);
      axios
        .get(apiUrl)
        .then((response) => {
          setLoading(false);
          if (response.data) {
              console.log(response.data);
            if (Object.keys(response.data).length === 0) {
                onEmptyDatasets(false)
            } else {
                onEmptyDatasets(true)
            }
            setPopulationData(response.data);
          }
        })
        .catch((error) => {
          setLoading(false);
          console.log(error);
        });
    };

    useEffect(() => {
      fetchPopulationCategoryData();
    }, [propertyId, startYear, endYear, selectedSpecies]);

    const data = processChartData(populationData);

    const options = {
        indexAxis: "y",
        plugins: {
            skipNull: true,
            responsive: true,
            maintainAspectRatio: false,
            datalabels: {
                display: false,
            },
            legend: {
                display: true,
                position: 'right' as 'right',
                labels: {
                    boxWidth: 20,
                    boxHeight: 13,
                    padding: 12,
                    font: {
                        size: 10,
                    },
                },
            },
            title: {
                display: true,
                text: `Number of properties per population category for ${selectedSpecies}`,
                font: {
                    size: 16,
                    weight: 'bold' as 'bold',
                },
            },
        },
        layout: {
            padding: {
                top: 0, // Remove top padding
            },
        },
        scales: {
            y: {
                skipNull: true,
                beginAtZero: true,
                stacked: false,
                title: {
                    display: true,
                    text: 'Population category',
                    font: {
                        size: 14,
                    },
                },
            },
            x: {
                beginAtZero: true,
                stacked: false,
                type: 'linear' as 'linear',
                title: {
                    display: true,
                    text: 'Number of properties (count)',
                    font: {
                        size: 14,
                    },
                },
                ticks: {
                    stepSize: 1, // Ensure whole number ticks
                    max: Math.ceil(200), // Round up to the nearest whole number
                },
            },
        },
    };


return (
    <Grid>
        {!loading ? (
            <Bar
                data={data}
                // @ts-ignore
                options={options}
            />
        ) : (
            <Loading containerStyle={{ minHeight: 160 }} />
        )}
    </Grid>
);
};

export default PopulationCategoryChart;
