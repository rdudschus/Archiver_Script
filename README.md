# How to Use


- from archapp.interactive import EpicsArchive
- Create an object calling the EpicsArchive class --> arch = EpicsArchive()
- To pull data from the archiver, use the 'get' function in EpicsArchive
	   data = arch.get("pv name" or ["pv1","pv2",...], start, end, xarray=True)
  Calling data returns a Pandas Dataframe of the PV's vals, severity, status.
- To get the vals --> data['pv name']['vals']
	Use this in functions.stats to get the mean, standard deviation, and variance.
		functions.stats(data['pv name']['vals'])
