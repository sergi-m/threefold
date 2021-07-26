#!/usr/bin/python

import os
import pandas as pd

from templates import tpl_main, tpl_test
import arg_parser


def main():
    """
    Gets the show on the road.
    """ 
    # load arguments
    args = arg_parser.parse_args()
    
    # check that files provided exist
    if not os.path.isfile(args.pdb_file):
            sys.exit("Error: PDB file was not found.")
    if not os.path.isfile(args.var_file):
            sys.exit("Error: variant file was not found.")
            
    # obtain data
    with open(args.var_file, 'r') as f:
        var_file = pd.read_csv(f)
        return mapped[cols]
            
    # generate script name
    output_file = f"{args.id}_var.cxc"
    output = os.path.join(args.output, output_file) if args.output \
        else os.path.join(os.getcwd(), output_file)
    
    # if overwrite option not selected, raise error if file in path exists
    if not args.overwrite:
        if os.path.isfile(output):
            sys.exit("Error: ChimeraX script already exists. To overwrite the existing script" \
                     "use the argument '--overwrite'")       
    
    # write cxc script using the template filled with details
    with open(output, "w") as f:
        f.write(template.format(**details))
        
    
      
if __name__ == '__main__':
    main()