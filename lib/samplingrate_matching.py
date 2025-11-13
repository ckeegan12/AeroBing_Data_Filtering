import numpy as np
class sample_rate_matching:
  def array_to_match(fast_data, fast_time, slow_data, slow_time, downsample=True):
      """
      Downsample the faster dataset to match the slower dataset's sampling rate.
      Clips both datasets to the shorter time duration.

      Parameters: Fast_data: arry of higher sampling rate data
                  fast_time: array of time points for fast_data
                  slow_data: array of lower sampling rate data
                  slow_time: array of time points for slow_data, 
      """
      
      # Convert to numpy arrays
      fast_data = np.array(fast_data)
      fast_time = np.array(fast_time)
      slow_data = np.array(slow_data)
      slow_time = np.array(slow_time)
      
      # Find overlap
      start_time = max(slow_time.min(), fast_time.min())
      end_time   = min(slow_time.max(), fast_time.max())

      # Clip both datasets to the shared range
      slow_mask = (slow_time >= start_time) & (slow_time <= end_time)
      fast_mask = (fast_time >= start_time) & (fast_time <= end_time)

      slow_time_clipped = slow_time[slow_mask]
      slow_data_clipped = slow_data[slow_mask]

      fast_time_clipped = fast_time[fast_mask]
      fast_data_clipped = fast_data[fast_mask]
            
      # Interpolate fast data to match 
      if downsample:
        fast_resampled = np.interp(slow_time_clipped, fast_time_clipped, fast_data_clipped)
        return fast_resampled, slow_data_clipped, slow_time_clipped
      else: 
        slow_resampled = np.interp(fast_time_clipped, slow_time_clipped, slow_data_clipped)
        return fast_data_clipped, slow_resampled, fast_time_clipped