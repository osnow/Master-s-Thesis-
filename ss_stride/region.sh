touch 169-178_for_seqLogo.dat
cut -c 169-178 3RIF_GLU_IVM_md1_nospace.dat >> 169-178_for_seqLogo.dat
sed -i '' '/^[A-Z]/i \
> \
' 169-178_for_seqLogo.dat
sed -i '' 's/./& /g' 169-178_for_seqLogo.dat
weblogo/seqlogo -f 169-178_for_seqLogo.dat -c -e -a -p -F PDF -h 5 -w 10 > 169-178_for_seqLogo.pdf

