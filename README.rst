**Harmonize-With-Midi**
#######################


**What it does:**

You input a midi file and a diatonic interval, it outputs a new midi file that harmonizes with the input.


**Usage**

.. code:: bash

    $ python harmonize.py test.mid 3  # test (harmonize using thirds)

	$ python harmonize.py -h # see the help info.
	
	
**Known Issues:**

If your midi is not quantized, you may wish to use the -f (--fix_timing) flag.

	
*MIT Licensed.*
