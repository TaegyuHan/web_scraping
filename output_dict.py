def make_dictionary(
    make_product_information_list, make_product_information_contents_list
):
    make_product_information_dict = {}
    make_product_information_len = len(make_product_information_list)
    for num in range(make_product_information_len):
        make_product_information_dict[
            make_product_information_list[num]
        ] = make_product_information_contents_list[num]
    return make_product_information_dict
