#Loc Nguyen

#functions takes in str and user defined frame size

def fifo(reference_string, frame_size):
    frames = []
    page_faults = 0
    result = []
    
    for page in reference_string:
        if page not in frames:
            if len(frames) >= frame_size:
                frames.pop(0)  # Remove the oldest page
            frames.append(page)
            page_faults += 1
        result.append(list(frames))  # Store the state of frames after each access
    
    return result, page_faults

def lru(reference_string, frame_size):
    frames = []
    page_faults = 0
    result = []
    
    for page in reference_string:
        if page not in frames:
            if len(frames) >= frame_size:
                frames.pop(0)  # Remove the least recently used page
            frames.append(page)
            page_faults += 1
        else:
            frames.remove(page)
            frames.append(page)  # Move the accessed page to the end of the list (recently used)
        
        result.append(list(frames))  # Store the state of frames after each access
    
    return result, page_faults

def optimal(reference_string, frame_size):
    frames = []
    page_faults = 0
    result = []
    
    for i, page in enumerate(reference_string):
        if page not in frames:
            if len(frames) >= frame_size:
                # Find the page that will not be used for the longest period of time
                farthest = -1
                index_to_remove = -1
                for j in range(len(frames)):
                    try:
                        next_use = reference_string[i+1:].index(frames[j]) + i + 1
                    except ValueError:
                        next_use = float('inf')  # If the page is not used again
                    if next_use > farthest:
                        farthest = next_use
                        index_to_remove = j
                frames.pop(index_to_remove)  # Remove the farthest page
            frames.append(page)
            page_faults += 1
        result.append(list(frames))  # Store the state of frames after each access
    
    return result, page_faults

# Read the test data file
def read_test_data(filename=r"C:\Users\locng\Documents\Github\CS_4310_OS\Project_2\data.txt"):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Display function to print the results in a table format
def display_results(algorithm_name, reference_string, frames_results, page_faults, frame_size):
    print(f"\n{algorithm_name} - Frame Size: {frame_size}")
    print(f"Reference String: {reference_string}")
    print("Step | Page Frames")
    print("----------------------")
    for i, frames in enumerate(frames_results):
        step = i + 1
        print(f"{step:4} | {frames} {'*' if reference_string[i] not in frames else ' '}")
    print(f"Total Page Faults: {page_faults}")
    print("-" * 30)

#
def main():
    reference_strings = read_test_data()
    frame_sizes = [3,4,5,6]
    
    for frame_size in frame_sizes:
        fifo_sum, lru_sum, opt_sum = 0,0,0
        for reference_string in reference_strings:
            # FIFO
            fifo_results, fifo_faults = fifo(reference_string, frame_size)     
            #display_results("FIFO", reference_string, fifo_results, fifo_faults, frame_size)
            fifo_sum += fifo_faults
            # LRU
            lru_results, lru_faults = lru(reference_string, frame_size)
            #display_results("LRU", reference_string, lru_results, lru_faults, frame_size)
            lru_sum += lru_faults
            # Optimal
            optimal_results, optimal_faults = optimal(reference_string, frame_size)
            #display_results("OPTIMAL", reference_string, optimal_results, optimal_faults, frame_size)
            opt_sum += optimal_faults

        #calculate avg 
        fifo_avg = fifo_sum / 50 
        lru_avg = lru_sum / 50 
        opt_avg = opt_sum / 50
        #display result
        print("Frame size: ", frame_size)
        print("FIFO: ",fifo_avg)
        print("LRU: ", lru_avg)
        print("Optimal: ", opt_avg)

if __name__ == "__main__":
    main()
