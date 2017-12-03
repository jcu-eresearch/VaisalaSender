import sensor_cloud

sensor_cloud.configuration.username = 'username'
sensor_cloud.configuration.password = 'password'

sensor_id_prefix = "sensor_id"

organisation = "org_name"
location = "locateion"
reporting_period = "PT15M"
sample_period = "P3Y"

streams = {
    "rain.accumulation": {
        "unitOfMeasure": "http://registry.it.csiro.au/def/qudt/1.1/qudt-unit/Millimeter",
        "observedProperty": "http://data.sense-t.org.au/registry/def/sop/Rain",
        "interpolationType": "http://www.opengis.net/def/waterml/2.0/interpolationType/Continuous",
        "samplePeriod": sample_period,
        "reportingPeriod": reporting_period,
        "organisation": organisation,
        "location": location
    },
    "rain.intensity": {
        "unitOfMeasure": "http://registry.it.csiro.au/def/environment/unit/MillimeterPerHour",
        "observedProperty": "http://data.sense-t.org.au/registry/def/sop/RainfallRate",
        "interpolationType": "http://www.opengis.net/def/waterml/2.0/interpolationType/Continuous",
        "samplePeriod": sample_period,
        "reportingPeriod": reporting_period,
        "organisation": organisation,
        "location": location
    },
    "temperature": {
        "unitOfMeasure": "http://registry.it.csiro.au/def/qudt/1.1/qudt-unit/DegreeCelsius",
        "observedProperty": "http://registry.it.csiro.au/def/environment/property/air_temperature",
        "interpolationType": "http://www.opengis.net/def/waterml/2.0/interpolationType/Continuous",
        "samplePeriod": sample_period,
        "reportingPeriod": reporting_period,
        "organisation": organisation,
        "location": location
    },
    "humidity": {
        "unitOfMeasure": "http://registry.it.csiro.au/def/qudt/1.1/qudt-unit/Percent",
        "observedProperty": "http://data.sense-t.org.au/registry/def/sop/RelativeHumidity",
        "interpolationType": "http://www.opengis.net/def/waterml/2.0/interpolationType/Continuous",
        "samplePeriod": sample_period,
        "reportingPeriod": reporting_period,
        "organisation": organisation,
        "location": location
    },
    "pressure": {
        "unitOfMeasure": "http://data.sense-t.org.au/registry/def/su/HectoPascal",
        "observedProperty": "http://registry.it.csiro.au/def/environment/property/air_pressure",
        "interpolationType": "http://www.opengis.net/def/waterml/2.0/interpolationType/Continuous",
        "samplePeriod": sample_period,
        "reportingPeriod": reporting_period,
        "organisation": organisation,
        "location": location
    },
    "wind.direction.average": {
        "unitOfMeasure": "http://registry.it.csiro.au/def/qudt/1.1/qudt-unit/DegreeAngle",
        "observedProperty": "http://data.sense-t.org.au/registry/def/sop/WindDirection",
        "interpolationType": "http://www.opengis.net/def/waterml/2.0/interpolationType/Continuous",
        "samplePeriod": sample_period,
        "reportingPeriod": reporting_period,
        "organisation": organisation,
        "location": location
    },
    "wind.direction.min": {
        "unitOfMeasure": "http://registry.it.csiro.au/def/qudt/1.1/qudt-unit/DegreeAngle",
        "observedProperty": "http://data.sense-t.org.au/registry/def/sop/WindDirection",
        "interpolationType": "http://www.opengis.net/def/waterml/2.0/interpolationType/Continuous",
        "samplePeriod": sample_period,
        "reportingPeriod": reporting_period,
        "organisation": organisation,
        "location": location
    },
    "wind.direction.max": {
        "unitOfMeasure": "http://registry.it.csiro.au/def/qudt/1.1/qudt-unit/DegreeAngle",
        "observedProperty": "http://data.sense-t.org.au/registry/def/sop/WindDirection",
        "interpolationType": "http://www.opengis.net/def/waterml/2.0/interpolationType/Continuous",
        "samplePeriod": sample_period,
        "reportingPeriod": reporting_period,
        "organisation": organisation,
        "location": location
    },
    "wind.speed.average": {
        "unitOfMeasure": "http://registry.it.csiro.au/def/qudt/1.1/qudt-unit/MeterPerSecond",
        "observedProperty": "http://data.sense-t.org.au/registry/def/sop/WindSpeed",
        "interpolationType": "http://www.opengis.net/def/waterml/2.0/interpolationType/Continuous",
        "samplePeriod": sample_period,
        "reportingPeriod": reporting_period,
        "organisation": organisation,
        "location": location
    },
    "wind.speed.max": {
        "unitOfMeasure": "http://registry.it.csiro.au/def/qudt/1.1/qudt-unit/MeterPerSecond",
        "observedProperty": "http://data.sense-t.org.au/registry/def/sop/WindSpeed",
        "interpolationType": "http://www.opengis.net/def/waterml/2.0/interpolationType/Continuous",
        "samplePeriod": sample_period,
        "reportingPeriod": reporting_period,
        "organisation": organisation,
        "location": location
    },
    "wind.speed.min": {
        "unitOfMeasure": "http://registry.it.csiro.au/def/qudt/1.1/qudt-unit/MeterPerSecond",
        "observedProperty": "http://data.sense-t.org.au/registry/def/sop/WindSpeed",
        "interpolationType": "http://www.opengis.net/def/waterml/2.0/interpolationType/Continuous",
        "samplePeriod": sample_period,
        "reportingPeriod": reporting_period,
        "organisation": organisation,
        "location": location
    }
}

LOGGING_FORMAT = '%(asctime)-15s %(levelname)-7s %(process)-6d %(name)s %(filename)s:%(funcName)s:%(lineno)d - %(message)s'
