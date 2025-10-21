from dataclasses import dataclass

import xarray as xr


@dataclass
class DomainGeometry:
    """
    Represents the geographical description of a domain for grid construction.

    Attributes:
        minimum_latitude: The minimum latitude of the domain.
        maximum_latitude: The maximum latitude of the domain.
        minimum_longitude: The minimum longitude of the domain.
        maximum_longitude: The maximum longitude of the domain.
    """

    minimum_latitude: float
    maximum_latitude: float
    minimum_longitude: float
    maximum_longitude: float


class EMODnetBathymetryDownloader:
    """
    A class to facilitate downloading bathymetry data from the EMODnet ERDDAP
    server.


    Attributes:
        URL (str): The URL of the EMODnet bathymetry dataset.

    Args:
        domain: The geographical domain for which bathymetry data is required.
    """

    URL: str = (
        "https://erddap.emodnet.eu/erddap/griddap/dtm_2020_v2_e0bf_e7e4_5b8f"
    )

    def __init__(self, domain: DomainGeometry):
        self._domain = domain

    def download_data(self) -> xr.Dataset:
        """
        Downloads bathymetry data for the specified geographical domain and
        returns it as an xarray dataset.
        """
        lon_slice = slice(
            self._domain.minimum_longitude, self._domain.maximum_longitude
        )
        lat_slice = slice(
            self._domain.minimum_latitude, self._domain.maximum_latitude
        )
        ds = xr.open_dataset(self.URL).sel(
            longitude=lon_slice, latitude=lat_slice
        )

        return ds


def main():
    domain = DomainGeometry(
        minimum_latitude=34.0,
        maximum_latitude=42.0,
        minimum_longitude=-10.0,
        maximum_longitude=2.0,
    )
    downloader = EMODnetBathymetryDownloader(domain)
    dataset = downloader.download_data()
    print(dataset)


if __name__ == "__main__":
    main()
