include makeinclude

OBJ	= main.o

all: coreval

coreval: $(OBJ)
	$(LD) $(LDFLAGS) -o coreval $(OBJ) $(LIBS)

clean:
	rm -f *.o coreval

makeinclude:
	@echo please run ./configure
	@false

SUFFIXES: .cpp .o
.cpp.o:
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $<
