import numpy as np
import pandas as pd

class SampleRateMatching:
    def __init__(self, fast_data_df = None, slow_data_df = None):
        self.fast_data_df = fast_data_df
        self.slow_data_df = slow_data_df
        
    def array_to_match(self, fast_data_df = None, slow_data_df = None, downsample=True):
        """
        Downsample the faster dataset to match the slower dataset's sampling rate.
        Clips both datasets to the shorter time duration.

        Parameters: 
            fast_data_df: DataFrame with time index and data columns
            slow_data_df: DataFrame with time index and data columns
            downsample: If True, downsample fast to slow rate. If False, upsample slow to fast rate.
        
        Returns:
            Tuple of (resampled_fast_data, resampled_slow_data, common_time)
        """
        # Extract time indices
        fast_time = fast_data_df.index.to_numpy()
        slow_time = slow_data_df.index.to_numpy()

        # Find overlap
        start_time = max(slow_time.min(), fast_time.min())
        end_time = min(slow_time.max(), fast_time.max())

        # Clip both datasets to the shared range
        slow_mask = (slow_time >= start_time) & (slow_time <= end_time)
        fast_mask = (fast_time >= start_time) & (fast_time <= end_time)

        slow_time_clipped = slow_time[slow_mask]
        slow_data_clipped = slow_data_df[slow_mask].to_numpy()

        fast_time_clipped = fast_time[fast_mask]
        fast_data_clipped = fast_data_df[fast_mask].to_numpy()
        
        # Interpolate to match sampling rates
        if downsample:
            # Downsample fast data to slow sampling rate
            if fast_data_clipped.ndim == 1:
                fast_resampled = np.interp(slow_time_clipped, fast_time_clipped, fast_data_clipped)
            else:
                fast_resampled = np.column_stack([
                    np.interp(slow_time_clipped, fast_time_clipped, fast_data_clipped[:, i])
                    for i in range(fast_data_clipped.shape[1])
                ])
            return fast_resampled, slow_data_clipped, slow_time_clipped
        else:
            if slow_data_clipped.ndim == 1:
                slow_resampled = np.interp(fast_time_clipped, slow_time_clipped, slow_data_clipped)
            else:
                # Handle multiple columns
                slow_resampled = np.column_stack([
                    np.interp(fast_time_clipped, slow_time_clipped, slow_data_clipped[:, i])
                    for i in range(slow_data_clipped.shape[1])
                ])
            return fast_data_clipped, slow_resampled, fast_time_clipped