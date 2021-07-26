#!/usr/bin/python

import argparse


def parse_args() -> argparse.Namespace: 
    """
    Parses arguments provided to the tool via the command line and stores them for later use.

    Returns:
        argparse.Namespace: information provided through the command line arguments.
    """  
    parser = argparse.ArgumentParser(description="""threefold maps variants at protein level to a PDB 
                                     downloaded from the AlphaFold Protein Structure Database and 
                                     generates a ChimeraX script to visualize them in 3D.""")
    
    parser.add_argument('-p', '--pdb_file',
                        required=True,
                        nargs='+',
                        help="""Path to the PDB file downloaded from the AlphaFold DB.""",
                        action='store',
                        type=str,
                        metavar='<string>',
                        dest='pdb_file')
    
    parser.add_argument('-f', '--var_file',
                        required=True,
                        nargs='+',
                        help="""Path to the variant file.""",
                        action='store',
                        type=str,
                        metavar='<string>',
                        dest='var_file')
    
    parser.add_argument('-i', '--id',
                        required=True,
                        nargs='+',
                        help="""ID by which the protein is identified in the variant file.""",
                        action='store',
                        type=str,
                        metavar='<string>',
                        dest='id')
    
    parser.add_argument('-h', '--hgvs',
                        required=True,
                        nargs='+',
                        help="""Name of column containing variants at protein level in HVGS format.""",
                        action='store',
                        type=str,
                        metavar='<string>',
                        dest='hgvs')
    
    parser.add_argument('-o', '--output',
                        required=False,
                        help='Output folder in which the cxc script will be saved.',
                        action='store',
                        type=str,
                        metavar='<string>',
                        dest='output')
    
    parser.add_argument('--overwrite',
                        required=False,
                        help='Script will overwrite output file.',
                        action='store_true',
                        dest='overwrite')
    
    
    
    

    return parser.parse_args()