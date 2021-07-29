#!/usr/bin/env python

import os
import pandas as pd
import re
import sys

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
            
    # obtain variant data
    with open(args.var_file, 'r') as f:
        var_file = pd.read_csv(f)
        
    # filter rows by given ID (present in any column)
    id_data = var_file[var_file.eq(args.id).any(axis=1)]
    print(f"Found {id_data.shape[0]} rows with given ID.")
    
    # extract variants and classify them 
    variants = [str(var) for var in id_data[args.var] if str(var) not in ("nan", 'p.0?')]
    
    silent_vars = [var for var in variants if "=" in var]
    fs_vars = [var for var in variants if 'fs*' in var]
    del_vars = [var for var in variants if "del" in var and var not in fs_vars]
    nonsense_vars = [var for var in variants if '*' in var and var not in fs_vars]
    missense_vars = [var for var in variants if var not in silent_vars + fs_vars \
        + del_vars + nonsense_vars]
    
    print(f"silent: {silent_vars}")
    print(f"fs: {fs_vars}")
    print(f"del: {del_vars}")
    print(f"nonsense: {nonsense_vars}")
    print(f"missense: {missense_vars}")
    
    # extract positions
    silent_pos = [re.search(r'\d+', var).group(0) for var in silent_vars]
    fs_pos = [re.search(r'\d+', var).group(0) for var in fs_vars]
    del_pos = [re.search(r'\d+', var).group(0) for var in del_vars]
    nonsense_pos = [re.search(r'\d+', var).group(0) for var in nonsense_vars]
    missense_pos = [re.search(r'\d+', var).group(0) for var in missense_vars]
    
    print(f"silent: {silent_pos}")
    print(f"fs: {fs_pos}")
    print(f"del: {del_pos}")
    print(f"nonsense: {nonsense_pos}")
    print(f"missense: {missense_pos}")
    
    # curate details to fill template
    details = {
        'id': args.id,
        'pdb_file': args.pdb_file,
        'silent': ",".join(str(pos) for pos in silent_pos) if silent_pos else 0,
        'missense': ",".join(str(pos) for pos in missense_pos) if missense_pos else 0,
        'nonsense': ",".join(str(pos) for pos in nonsense_pos) if nonsense_pos else 0,
        'deletion': ",".join(str(pos) for pos in del_pos) if del_pos else 0,
        'frameshift': ",".join(str(pos) for pos in fs_pos) if fs_pos else 0
    }
                
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
    with open(output, "w+") as f:
        f.write(tpl_main.format(**details))
        
    
if __name__ == '__main__':
    main()