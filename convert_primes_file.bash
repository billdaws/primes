prime_file=$1
out_file=$2
cat ${prime_file} | sed '/primes.utm.edu/d' \ # delete header line
    | sed -E -e 's/[[:blank:]]+/\n/g' \ # replace weird whitespace with newline
    | sed -E -e '/^[[:space:]]*$/d' \ # delete empty lines
    > ${out_file}