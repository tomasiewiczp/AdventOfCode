PATH='day_5/input2.txt'

def load_input(path):
    with open(path,'r') as file:
        return file.readlines()
    
class Seed_plan:
    def __init__(self,input_data) -> None:
        """
        Initializes the Seed_plan class with input data.

        Parameters:
        input_data (list): A list of strings representing the input data.

        Returns:
        None
        """
        self.seeds=[int(seed) for seed in input_data[0].split()[1:]]
        self.maps={}
        values=[]
        self.locations=[]
        self.queue=[]
        for s in input_data[2:]:
            if s[0].isalpha():
                name=s.split()[0].replace("-to-",'_')
                self.queue.append(s.split()[0].split('-')[0])
                if s.split()[0].split('-')[0]=='humidity':
                    self.queue.append(s.split()[0].split('-')[2])
            elif s[0].isdigit():
                values.append([int(val) for val in s.rstrip().split()])
            else :
                self.maps[name]=values
                values=[]

    def map_seed(self):
        """
        Calculates the minimum location of seeds based on the mappings.

        Parameters:
        None

        Returns:
        None
        """
        for seed in self.seeds:
            for count, mapping in enumerate(self.queue[:-1]):
                potential_changes = self.maps[self.queue[count] + '_' + self.queue[count + 1]]
                for tab in potential_changes:
                    if seed in range(tab[1], tab[1] + tab[2]):
                        seed -= (tab[1] - tab[0])
                        break
            self.locations.append(seed)

    def get_result(self):
        """
        Returns the minimum location of seeds.

        Parameters:
        None

        Returns:
        int: The minimum location of seeds.
        """
        return min(self.locations)
    
data=load_input(PATH)
s=Seed_plan(data)
s.map_seed()
print(s.get_result())